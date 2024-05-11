from tests.bast1aan.site import tags

tags.tags.append(tags.Tag(value='index'))

def view():
	return {'tags': tags.tags}
