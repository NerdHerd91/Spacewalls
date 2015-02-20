import run, json, datetime

def load_pics(session):
	pic_files = ['./app/static/images/spacex.json', './app/static/images/hubble.json']
	for pic_file in pic_files:
		with open(pic_file) as f:
			decoded_json = json.load(f)

			for i in decoded_json:
				path = 'static/images/' + i['title']
				url = i['link'] 
				last_modified = datetime.datetime.now()

				entry = run.Wallpapers(path=path, url=url, last_modified=last_modified)
				session.add(entry)
			session.commit()


def main(session):
	run.Base.metadata.create_all(bind=run.engine)
	load_pics(session)

if __name__ == "__main__":
	main(run.session)
			
			

