ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

class EmailForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
	form = EmailForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			# if check_password_hash(user.password, form.password.data):
			# 	login_user(user, remember=form.remember.data)
			# 	return redirect(url_for('scrapelist2'))

			email_list = 'xxx'

			user_name = form.username.data
			message_all = 'Hi ' + user_name + '!' + '\n' + '\n' + 'Heres your Password Reset link!' + '\n' + 'If you have any questions or things you would like to report, please email surfsendhelp@gmail.com.' + '\n' + '\n' + 'Warm Regards,' + '\n' + '	-Team SurfSend'

			msg = MIMEMultipart()
			msg['From'] = 'xxx'
			msg['To'] = 'xxx'
			msg['Subject'] = 'Thanks for Registering!'
			# message = j + 'ft' ' @ ' + k + ' on ' + l
			# print(message)
			msg.attach(MIMEText(message_all))

			mailserver = smtplib.SMTP('smtp.gmail.com',587)
			# identify ourselves to smtp gmail client
			mailserver.ehlo()
			# secure our email with tls encryption
			mailserver.starttls()
			# re-identify ourselves as an encrypted connection
			mailserver.ehlo()
			mailserver.login('xxx', 'xxx')

			mailserver.sendmail('xxx',email_list,msg.as_string())

			mailserver.quit()
			flash('PW Reset Email Sent!')







		flash('Invalid Username/Password')
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

	return render_template('forgot.html', form=form)