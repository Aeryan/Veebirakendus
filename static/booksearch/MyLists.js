var owntable = document.getElementById('owntable');
var wanttable = document.getElementById('wanttable');
var pealkiri = document.getElementById('pealkiri');
var tekst = document.getElementById('tekst');
var pilt = document.getElementById('pilt');
var valik;

for (var i = 0; i < owntable.rows.length; i++) {
    owntable.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        pealkiri.innerHTML = "<h2>" + valik + "</h2>";
        tekst.innerHTML = "<p>Henry on üks hirmus poiss, arvavad täiskasvanud. Aga Henry ise ei tee sellest välja. Tema korraldatud ettevõtmistest ja tempudest see ja järgnevad Hirmsa Henry sarja raamatud räägivadki. Isegi kui Henry püüab olla oma venna Perfektse Peteri moodi või käia balletitunnis, on tulemus ikka võrdlemisi hirmus.</p>";
        pilt.innerHTML = '<img src="https://elisaveeb-file.elisa.ee/files/book_images/9789949781072_hirmus-henry-esimene-raamat-sari-hirmus-henri_430.jpg" alt="Hirmus Henry">';
        document.getElementById('rmWantedForm').style.display='none';
    }
}

for (var i = 0; i < wanttable.rows.length; i++) {
    wanttable.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        pealkiri.innerHTML = "<h2>" + valik + "</h2>";
        tekst.innerHTML = "<p>Henry on üks hirmus poiss, arvavad täiskasvanud. Aga Henry ise ei tee sellest välja. Tema korraldatud ettevõtmistest ja tempudest see ja järgnevad Hirmsa Henry sarja raamatud räägivadki. Isegi kui Henry püüab olla oma venna Perfektse Peteri moodi või käia balletitunnis, on tulemus ikka võrdlemisi hirmus.</p>";
        pilt.innerHTML = '<img src="https://elisaveeb-file.elisa.ee/files/book_images/9789949781072_hirmus-henry-esimene-raamat-sari-hirmus-henri_430.jpg" alt="Hirmus Henry">';
        document.getElementById('rmWantedForm').style.display='block';
    }
}