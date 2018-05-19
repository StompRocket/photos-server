from bottle import route, run, post, get
from pymongo import MongoClient
import json


client = MongoClient()

db = client.photos

images = db.images

image_data = {
	'ownerid': 'asdf',
	'ownername': 'dave',
	'imgid': 'abcd1234',
	'imgcontent': 'image as bin',
	'imgtype': 'png'
}

result = images.insert_one(image_data)
print('One image: {0}'.format(result.inserted_id))

@route("/i/<uid>/<img>")
def returnImage(uid, img):
	image_result = images.find_one({'ownerid': uid, 'imgid': img})
	return str(image_result)


run(host='localhost', port=4242, debug=True)