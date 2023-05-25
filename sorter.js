let fs = require('fs');
const { extension } = require('mime');
let path =require('path')
let currentpath= 'C:/Users/Lisa/Downloads/';

fs.readdir(currentpath, dirRead);

function dirRead(err, files){
    console.log('read ' + currentpath);
    console.log(files);
    files.forEach(processfile);
}

function processfile(file){
    let extension = path.extname(file);
    console.log("extension is" + extension);
    fs.mkdir(currentpath + extension ,function(){
        console.log('creating Dir done');
        fs.rename(currentpath + file, currentpath + extension + "/" + file, fileCreated);
    });
}

  function fileCreated(){
    console.log('done');
  }

