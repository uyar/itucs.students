# -*- coding: utf-8 -*-

import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

from StringIO import StringIO


def generate(self, response):
    pdfmetrics.registerFont(TTFont('ITURegular', 'times.ttf'))
    pdfmetrics.registerFont(TTFont('ITUBold', 'timesbd.ttf'))

    o = 'hello.pdf'
    c = canvas.Canvas(o, pagesize=A4)

    c.setTitle('Ders Kayıt Dilekçesi')

    c.setFont('ITURegular', 11)

    xl = 50   # left x coordinate
    yt = 750  # top y coordinate
    lh = 15   # line height

    yc = yt

    antet = canvas.ImageReader(StringIO(open('antet.jpg', 'rb').read()))
    c.drawImage(antet, 450, 700, 78, 106)

    text = c.beginText(150, yc)
    text.setFont('ITURegular', 12)
    text.textLine("İTÜ Bilgisayar ve Bilişim Fakültesi Dekanlığına,")
    c.drawText(text)
    yc -= 2 * lh

    text = c.beginText(xl, yc)
    text.textLine('Aşağıda ayrıntılı bilgileri verilen derse, belirttiğim nedenden dolayı kayıt olamadım.')
    c.drawText(text)
    yc -= lh

    text = c.beginText(xl, yc)
    text.textLine('Fakülte web sayfasında duyurulan başvuru koşullarını sağlıyorum.')
    c.drawText(text)
    yc -= lh

    text = c.beginText(xl, yc)
    text.textLine('Bu derse kaydedilebilmem için gerekenin yapılmasını saygılarımla arz ederim.')
    c.drawText(text)
    yc -= 1.5 * lh

    text = c.beginText(xl, yc)
    text.textLine('Ek1. Not döküm belgesi (transkript)')
    c.drawText(text)
    yc -= lh

    text = c.beginText(xl, yc)
    text.textLine('Ek2. Haftalık ders çizelgesi')
    c.drawText(text)
    yc -= 2 * lh

    styles = getSampleStyleSheet()

    td = ParagraphStyle(name='TD', fontName='ITURegular', align=TA_LEFT)
    styles.add(td)

    th = ParagraphStyle(name='TH', fontName='ITUBold', align=TA_LEFT)
    styles.add(th)

    # Headers
    h_ogrenci = Paragraph("ÖĞRENCİ BİLGİLERİ", styles['TH'])
    h_ogrenci_no = Paragraph("Öğrenci No:", styles['TH'])
    h_ad_soyad = Paragraph("Adı ve Soyadı:", styles['TH'])
    h_fakulte = Paragraph("Fakültesi:", styles['TH'])
    h_bolum = Paragraph("Bölümü:", styles['TH'])
    h_telefon = Paragraph("İletişim Telefonu:", styles['TH'])
    h_e_posta = Paragraph("E-posta:", styles['TH'])
    h_tarih = Paragraph("Tarih:", styles['TH'])
    h_imza = Paragraph("İmza:", styles['TH'])

    h_ders = Paragraph("DERS BİLGİLERİ", styles['TH'])
    h_ders_kod_ve_ad = Paragraph("Dersin Kodu ve Adı:", styles['TH'])
    h_gun_ve_saat = Paragraph("Gün ve Saat:", styles['TH'])
    h_ders2 = [
        Paragraph("Varsa 2. seçenek dersin Kodu, Adı ve Zamanı:", styles['TH']),
        Paragraph("(Sadece yukarıdaki ders kabul edilmezse değerlendirilecektir.)", styles['TD'])
    ]
    h_gerekce = Paragraph("Gerekçesi:", styles['TH'])

    h_degerlendirme = [
        Paragraph("DEĞERLENDİRME", styles['TH']),
        Paragraph("(BU KISIM FAKÜLTE TARAFINDAN DOLDURULACAKTIR)", styles['TH'])
    ]
    h_gorus = Paragraph("Bölüm/Fakülte Görüşü:", styles['TH'])

    # Data
    d_ogrenci_no = Paragraph(self.ogrenci_no, styles['TD'])
    d_ad_soyad = Paragraph(self.ad_soyad, styles['TD'])
    d_fakulte = Paragraph(self.fakulte, styles['TD'])
    d_bolum = Paragraph(self.bolum, styles['TD'])
    d_telefon = Paragraph(self.telefon, styles['TD'])
    d_e_posta = Paragraph(self.e_posta, styles['TD'])
    d_tarih = Paragraph(self.tarih, styles['TD'])
    d_ders_kod_ve_ad = Paragraph('%s - %s' % (self.ders_kod, self.ders_ad),
                                 styles['TD'])
    d_gun_ve_saat = Paragraph(self.gun_ve_saat, styles['TD'])
    d_ders2 = Paragraph(self.ders2, styles['TD'])
    d_gerekce = Paragraph(self.gerekce, styles['TD'])

    data = [
        [h_ogrenci, ''],
        [h_ogrenci_no, d_ogrenci_no],
        [h_ad_soyad, d_ad_soyad],
        [h_fakulte, d_fakulte],
        [h_bolum, d_bolum],
        [h_telefon, d_telefon],
        [h_e_posta, d_e_posta],
        [h_tarih, d_tarih],
        [h_imza, ''],

        [h_ders, ''],
        [h_ders_kod_ve_ad, d_ders_kod_ve_ad],
        [h_gun_ve_saat, d_gun_ve_saat],
        [h_ders2, d_ders2],
        [h_gerekce, d_gerekce],

        [h_degerlendirme, ''],
        [h_gorus, '']
    ]

    rowHeights = 8*[None] + [1.5*cm] + 4*[None] + [3*cm] + [None] + [2*cm]
    table = Table(data, colWidths=[6*cm, 11*cm], rowHeights=rowHeights)
    style = TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('SPAN', (0, 0), (-1, 0)),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('SPAN', (0, 9), (-1, 9)),
        ('ALIGN', (0, 9), (-1, 9), 'CENTER'),
        ('BACKGROUND', (0, 9), (-1, 9), colors.lightgrey),
        ('SPAN', (0, 14), (-1, 14)),
        ('BACKGROUND', (0, 14), (-1, 14), colors.lightgrey),
    ])
    table.setStyle(style)

    table.wrapOn(c, *A4)
    table.drawOn(c, xl, 150)

    c.showPage()
    c.save()


class Record:
    def __init__(self):
        self.ogrenci_no = '150150001'
        self.ad_soyad = 'H. Turgut Uyar'
        self.fakulte = 'Bilgisayar ve Bilişim Fak.'
        self.bolum = 'Bilgisayar Müh. (%100 İng.)'
        self.telefon = '0212 2853632'
        self.e_posta = 'uyar@itu.edu.tr'
        self.tarih = '2016-08-13'
        self.ders_kod = 'BLG361E'
        self.ders_ad = 'Database Management Systems'
        self.gun_ve_saat = 'Çarşamba 09:30-12:30'
        self.ders2 = 'BLG361, Veri Tabanı Yönetim Sistemleri, Çarşamba 09:30-12:30'
        self.gerekce = 'Mağdur oldum.'


generate(Record(), None)
