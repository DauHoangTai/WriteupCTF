var socket = io();

socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

$(function() {
	$('#process').click(function(e){
		xpath = $('#xpath').val();
		xml = $('#xml').val();
		socket.emit('message', xpath, xml);
	});
});

socket.on('result', function(msg){
    alert(msg);
});