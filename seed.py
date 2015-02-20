import app, json, datetime

def load_pics(session):
	with open('./static/images/spacex.json') as f:
		decoded_json = json.load(f)

		for i in decoded_json:
			path = 'static/images/' + i['title']
			url = i['link'] 
			last_modified = datetime.datetime.now()

			entry = app.Wallpapers(path=path, url=url, last_modified=last_modified)
			session.add(entry)
		session.commit()


def main(session):
	app.Base.metadata.create_all(bind=app.engine)
	load_pics(session)

if __name__ == "__main__":
	main(app.session)
			
			

