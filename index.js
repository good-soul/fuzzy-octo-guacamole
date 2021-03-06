var express = require('express');
var formidable = require('formidable');
const { exec } = require('child_process')

const app = express();

app.use(express.static(__dirname+'/public'));

app.post('/fileupload', function(req,res){
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
	console.log(fields,files)
        const filepath = files.file.filepath
        const command = `python3 Webcam_Prediction/step_10_staticImage_v4_fastai_Test.py ${filepath} ${fields.y1} ${fields.y2} ${fields.x1} ${fields.x2}`
        exec(command, (error, stdout, stderr) => {
	    //console.log(fields);
            if(error){
                console.log(`error: ${error.message}`);
                return
            }
            if(stderr){
                console.log(`stderr: ${stderr}`);
                return
            }
	    res.type('text/html');
            res.write(`${stdout}`);
            res.end();
	    exec(`rm ${filepath}`);
        })
    })
})
app.listen(7777, function(){
    console.log('Server started on port 7777');
})
