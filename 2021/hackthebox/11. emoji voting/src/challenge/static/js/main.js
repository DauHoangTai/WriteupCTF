const emojis = document.getElementById('emojis');

const addEmoji = emoji => {
	const template = `
		<div class="col card card-nginx" onclick="vote(${ emoji.id })">
			<p class="card-title">${ emoji.name }</p>
			<div class="card-data">
				<div class="card-sub">
					<p class="data">${ emoji.emoji }</p>
				</div>
				<div class="card-sub">
					<p class="counts">${ emoji.count } votes</p>
				</div>
			</div>
		</div>
	`;

	emojis.insertAdjacentHTML('beforeend', template);
};

const getEmojis = () => {
	fetch('/api/list', {
        method: 'POST',
        body: JSON.stringify({
            order: 'count DESC'
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
	.then(res => res.json())
	.then(data => {
		emojis.innerHTML = '';
		data.forEach(emoji => {
			addEmoji(emoji);
		});
	})
};

const vote = (id) => {
    fetch('/api/vote', {
        method: 'POST',
        body: JSON.stringify({
            id: id
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => {
        if (res.ok) {
            update();
        }
    })
}

const update = () => getEmojis();

update();
setInterval(update, 5000);