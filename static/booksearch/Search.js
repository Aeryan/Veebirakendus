var table = document.getElementById('table');
var parem = document.getElementById('parem');
var valik;

for (var i = 0; i < table.rows.length; i++) {
    table.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        parem.innerHTML = "<p>Selle raamatu pealkiri on \"" + valik + "\".</p>";
        document.getElementById('ownedForm').style.display='block';
        document.getElementById('wantedForm').style.display='block';
    }
}