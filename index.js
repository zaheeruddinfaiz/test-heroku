const child_process = require('child_process');
const express=require('express')
const app = express()
app.get('/',async(req,res)=>{
    const result = await run_python_script();
    res.send(result);
})
async function run_python_script() {
    return new Promise((resolve, reject)=>{
        stream = child_process.spawn('python', ['scraper.py'], { shell: true });
        
        stream.stdout.on('data',(data)=>{
            console.log('This is'+data.toString());
            resolve(data.toString())
        })
        stream.stderr.on('data',(error)=>{
            console.log(error.toString())
            reject(error.toString())
        })        
    })
}
app.listen(3000,'localhost');