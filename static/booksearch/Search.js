var table = document.getElementById('table');
var pealkiri = document.getElementById('pealkiri');
var tekst = document.getElementById('tekst');
var pilt = document.getElementById('pilt');
var valik;

function jpgerror() {
    let sorc = "/media/" + valik + ".png";
    pilt.innerHTML = '<img src="' + sorc + '" alt="Raamatu pilt" onerror="pngerror()">';
}
function pngerror() {
    let sorc = "/media/" + valik + ".gif";
    pilt.innerHTML = '<img src="' + sorc + '" alt="Raamatu pilt" onerror="giferror()">';
}
function giferror() {
    let sorc = "/media/" + valik + ".jpeg";
    pilt.innerHTML = '<img src="' + sorc + '" alt="Raamatu pilt" onerror="jpegerror()">';
}
function jpegerror() {
    let sorc = "/media/default.png";
    pilt.innerHTML = '<img src="' + sorc + '" alt="Raamatu pilt">';
}


for (var i = 0; i < table.rows.length; i++) {
    table.rows[i].onclick = function() {
        valik = this.cells[0].innerHTML;
        pealkiri.innerHTML = "<h2>" + valik + "</h2>";
        let sorc = "/media/" + valik + ".jpg";

        tekst.innerHTML = "<p>Henry on üks hirmus poiss, arvavad täiskasvanud. Aga Henry ise ei tee sellest välja. Tema korraldatud ettevõtmistest ja tempudest see ja järgnevad Hirmsa Henry sarja raamatud räägivadki. Isegi kui Henry püüab olla oma venna Perfektse Peteri moodi või käia balletitunnis, on tulemus ikka võrdlemisi hirmus.</p>";
        pilt.innerHTML = '<img src="' + sorc + '" alt="Hirmus Henry" onerror="jpgerror()">';
        document.getElementById('ownedForm').style.display='block';
        document.getElementById('wantedForm').style.display='block';
    }
}