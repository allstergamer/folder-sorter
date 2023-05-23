
//need fs module for this to work
let fs = require('fs');
const { extension } = require('mime');
let path =require('path')

// location of this project is C:\Users\Lisa\Downloads so i called it currentpath
let currentpath= 'C:/Users/Lisa/Downloads/';

fs.readdir(currentpath, dirRead);

// Reads the directory and logs the files to the console.
function dirRead(err, files){
    // Log the current path
    console.log('read ' + currentpath);
    // Log the files in the directory
    console.log(files);

    files.forEach(processfile);
    

}


//
function processfile(file){
    let extension = path.extname(file);
    console.log("extension is" + extension);
    fs.mkdir(currentpath + extension ,function(){
        console.log('creating Dir done');
        fs.rename(currentpath + file, currentpath + extension + "/" + file, fileCreated);
     
    });
}


//create file named datei1.txt in currentpath
//fs.appendFile(currentpath + '.tested/datei1.txt', 'x', fileCreated);



  //print done in console
  function fileCreated(){
    console.log('done');
  }
  //