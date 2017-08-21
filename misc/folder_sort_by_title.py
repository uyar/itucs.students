objs = list(context.listFolderContents())
objs.sort(key=lambda x: x.Title())
for i, obj in enumerate(objs):
    context.moveObjectToPosition(obj.id, i)

