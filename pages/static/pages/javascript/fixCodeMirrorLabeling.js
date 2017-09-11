window.addEventListener('load', function (){
	var panels = document.querySelectorAll('.panel.panel-info');
	for(var i = 0; i < panels.length; i++){
		var panel = panels[i];
		var label = panel.querySelector('label');
		var labelFor = label.getAttribute('for');
		console.log('panel: '+panel);
		console.log('label: '+label+'\nid:'+labelFor);
		var textareas = panel.querySelectorAll('textarea');
		if(label && labelFor && textareas[1]){
			textareas[1].id = labelFor;
		}
	}
});