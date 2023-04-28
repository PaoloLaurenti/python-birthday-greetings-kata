init:
	pip install -r requirements.txt

test:
	pytest tests

check-email-sending:
	PYTHONPATH="${PYTHONPATH}:$(pwd)" \
	SMTP_SERVER_ADDRESS="" \
	SMTP_SERVER_PORT= \
	SMTP_SERVER_LOGIN= \
	SMTP_SERVER_PASSWORD= \
	python script/check_send_real_emails.py
