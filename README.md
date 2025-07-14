1.Clone the Repository
	git clone https://github.com/ramserssesd/Real-Time-Collaborative-Document-Editor.git
2. Create and Activate a Virtual Environment
	python -m venv virtual
	virtual\Scripts\activate
3. Install Dependencies
	pip install -r requirements.txt
4. Apply Migrations
	python manage.py makemigrations
	python manage.py migrate
5. Create Superuser.
	python manage.py createsuperuser
6. Run the Development Server
	python manage.py runserver
