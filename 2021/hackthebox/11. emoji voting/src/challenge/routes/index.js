const path      = require('path');
const express   = require('express');
const router    = express.Router();

let db;

const response = data => ({ message: data });

router.get('/', (req, res) => {
	return res.sendFile(path.resolve('views/index.html'));
});

router.post('/api/vote', (req, res) => {
	let { id } = req.body;

	if (id) {
		return db.vote(id)
			.then(() => {
				return res.send(response('Successfully voted')) ;
			})
			.catch((e) => {
				return res.send(response('Something went wrong'));
			})
	}

	return res.send(response('Missing parameters'));
})

router.post('/api/list', (req, res) => {
	let { order } = req.body;

	if (order) {
		return db.getEmojis(order)
			.then(data => {
				if (data) {
					return res.json(data);
				}

				return res.send(response('Seems like there are no emojis'));
			})
			.catch((e) => {
				return res.send(response('Something went wrong'));
			})
	}

	return res.send(response('Missing parameters'))
});	

module.exports = database => { 
	db = database;
	return router;
};