var owntable = document.getElementById('owntable');
var wanttable = document.getElementById('wanttable');
var parem = document.getElementById('parem');
var valik;

for (var i = 0; i < owntable.rows.length; i++) {
    owntable.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        parem.innerHTML = "<p>Selle raamatu pealkiri on \"" + valik + "\".</p>";
        document.getElementById('rmWantedForm').style.display='none';
    }
}

for (var i = 0; i < wanttable.rows.length; i++) {
    wanttable.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        parem.innerHTML = "<p>Selle raamatu pealkiri on \"" + valik + "\".</p>";
        document.getElementById('rmWantedForm').style.display='block';
    }
}