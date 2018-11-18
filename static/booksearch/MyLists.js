var owntable = document.getElementById('owntable');
var wanttable = document.getElementById('wanttable');
var vasak = document.getElementById('vasak');
var pilt = document.getElementById('pilt');
var valik;

for (var i = 0; i < owntable.rows.length; i++) {
    owntable.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        vasak.innerHTML = "<p>Selle raamatu pealkiri on \"" + valik + "\".</p>";
        pilt.innerHTML = '<img src="https://elisaveeb-file.elisa.ee/files/book_images/9789949781072_hirmus-henry-esimene-raamat-sari-hirmus-henri_430.jpg" alt="Hirmus Henry">';
        document.getElementById('rmWantedForm').style.display='none';
    }
}

for (var i = 0; i < wanttable.rows.length; i++) {
    wanttable.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        vasak.innerHTML = "<p>Selle raamatu pealkiri on \"" + valik + "\".</p>";
        pilt.innerHTML = '<img src="https://elisaveeb-file.elisa.ee/files/book_images/9789949781072_hirmus-henry-esimene-raamat-sari-hirmus-henri_430.jpg" alt="Hirmus Henry">';
        document.getElementById('rmWantedForm').style.display='block';
    }
}