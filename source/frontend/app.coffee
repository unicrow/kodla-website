express = require 'express'
bodyParser = require 'body-parser'
Twit = require 'twit'
nodemailer = require 'nodemailer'
serveStatic = require 'serve-static'

# Mailer
nodemailer = require 'nodemailer'
contact = nodemailer.createTransport
	service: 'gmail'
	auth:
		user: 'kodlacoorg@gmail.com'
		pass: 'iM-v#S|2O=z?Lt'

sendEmail = (data) ->
	contact.sendMail data, (error, info) ->
		if error
			console.log error.message
		else
			console.log 'Message sent successfully!'

# Express Conf.
app = express()
app.use bodyParser.urlencoded { extended: false }
app.use bodyParser.json()

# Static Serve
app.use '/static/', serveStatic("#{__dirname}/static")

# Twitter Api
T = new Twit {
	consumer_key: 'RJK6IbUP4laVT1XMDJA2iooQI'
	consumer_secret: 'w63bE39LH6ZC6qK8961VXhVaCaQZQvGRxPjYtYtcUAkUFFEfIt'
	access_token: '115366693-rrDKvcofi3zXkQbqdqkvspnK32sbRVZVptIC3KsT'
	access_token_secret: 'vdGnmBal5QvR5K8gCpHpqui7u5lifmxDZeb9vtPcD4o2M'
}

options = {
	screen_name: 'kodlaco'
	count: 5
}

# Routes
app.get '/', (req, res)->
	res.sendFile "#{__dirname}/index.html"

app.get '/get-tweets', (req, res) ->
	T.get 'statuses/user_timeline', options, (err, data) ->
		res.json data # data.text: tweet's content

app.post '/send-mail', (req, res) ->

	if req.body.name and req.body.email and req.body.message
		sendEmail {
			to: ['info@kodla.co', 'contact@kodla.co', 'fatih@unicrow.com']
			subject: 'Kodla.co Contact Form'
			html: "Name: <b>#{req.body.name}</b> <br><br> Email: #{req.body.email} <br><br> Message: <b>#{req.body.message}</b>"
		}

		res.send true
	else
		res.send false


app.listen 2016, ->
	console.log "Server Started!"
