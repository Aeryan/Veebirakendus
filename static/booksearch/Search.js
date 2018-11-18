var table = document.getElementById('table');
var vasak = document.getElementById('vasak');
var pilt = document.getElementById('pilt');
var valik;

for (var i = 0; i < table.rows.length; i++) {
    table.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        vasak.innerHTML = "<p>Selle raamatu pealkiri on \"" + valik + "\".</p>";
        pilt.innerHTML = '<img src="https://elisaveeb-file.elisa.ee/files/book_images/9789949781072_hirmus-henry-esimene-raamat-sari-hirmus-henri_430.jpg" alt="Hirmus Henry">';
        document.getElementById('ownedForm').style.display='block';
        document.getElementById('wantedForm').style.display='block';
    }
}