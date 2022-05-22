hideWorkDis = false;
hideWorkMon = false;
hideWorkSlov = false;

document.querySelector('#dis').addEventListener('click', e => {   
    var listDis = document.getElementById('list-dis')
    var listMon = document.getElementById('list-mon')
    var listSlov = document.getElementById('list-slov')
    if (hideWorkDis == false){
        listDis.style.display = 'block';
        listMon.style.display = 'none';
        listSlov.style.display = 'none';
        hideWorkDis = true;
        hideWorkMon = false;
        hideWorkSlov = false;
        console.log(hideWorkSlov);
    }
    else{
        listDis.style.display = 'none';
        listMon.style.display = 'none';
        listSlov.style.display = 'none';
        hideWorkDis = false;
        hideWorkMon = false;
        hideWorkSlov = false;
        console.log(hideWorkSlov);
    }
});

document.querySelector('#mon').addEventListener('click', e => {   
    var listDis = document.getElementById('list-dis')
    var listMon = document.getElementById('list-mon')
    var listSlov = document.getElementById('list-slov')
    if (hideWorkMon == false){
        listDis.style.display = 'none';
        listMon.style.display = 'block';
        listSlov.style.display = 'none';
        hideWorkMon = true;
        hideWorkDis = false;
        hideWorkSlov = false;
        console.log(hideWorkSlov);
    }
    else{
        listDis.style.display = 'none';
        listMon.style.display = 'none';
        listSlov.style.display = 'none';
        hideWorkMon = false;
        hideWorkDis = false;
        hideWorkSlov = false;
        console.log(hideWorkSlov);
    }
});

document.querySelector('#slov').addEventListener('click', e => {   
    var listDis = document.getElementById('list-dis')
    var listMon = document.getElementById('list-mon')
    var listSlov = document.getElementById('list-slov')
    if (hideWorkSlov == false){
        listDis.style.display = 'none';
        listMon.style.display = 'none';
        listSlov.style.display = 'block';
        hideWorkSlov = true;
        hideWorkMon = false;
        hideWorkDis = false;
        console.log(hideWorkSlov);
    }
    else{
        listDis.style.display = 'none';
        listMon.style.display = 'none';
        listSlov.style.display = 'none';
        hideWorkSlov = false;
        hideWorkMon = false;
        hideWorkDis = false;
    }
});