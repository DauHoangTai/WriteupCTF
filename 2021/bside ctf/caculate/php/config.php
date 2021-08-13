<?php
if(isset($_GET['🐶'])) {
	highlight_file(__FILE__);
}
function filter($payload) {
	if (preg_match("/[a-zA-BD-Z!@#%^&*:'\"|`~\\\\]|3|5|6|9/",$payload)) {
		return true;
	}
}
?>
<!-- ?🐶 -->
