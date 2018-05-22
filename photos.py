from bottle import route, run, post, get
from pymongo import MongoClient
import json


client = MongoClient()

db = client.photos

images = db.images

image_data = {
	'ownerid': 'asdf',
	'imgid': 'abcd1234',
	'imgcontent': 'image as bin',
	'imgtype': 'png'
}

result = images[image_data[ownerid]].insert_one(image_data)
print('One image: {0}'.format(result.inserted_id))

@route("/i/<uid>/<img>")
def returnImage(uid, img):
	image_result = images[uid].find_one({'ownerid': uid, 'imgid': img})
	return str(image_result)
@post("/post/<uid>/<img>")
def postImage(uid, img):
	images
	post_content = request.body.read()
	post_data = {
		'ownerid': uid,
		'imgid': img,
		'imgcontent': post_content.imgcontent,
		'imgtype': post_content.imgtype
	}
	
	post_result = images[post_data.ownerid].insert_one(post_data)
	return post_result.inserted_id


run(host='localhost', port=4242, debug=True)
