const child_process = require('child_process');

async function run_python_script() {
    new Promise()
    return new Promise((resolve, reject)=>{
        stream = child_process.spawn('python', ['scraper.py'], { shell: true });
        
        stream.stdout.on('data',(data)=>{
            console.log('This is'+data.toString());
            resolve(data)
        })
        stream.stderr.on('data',(error)=>{
            console.log(error.toString())
            reject(error.toString())
        })        
    })
}
run_python_script().then((console.log('Data'))).catch((error)=>{
    console.log('This'+error.toString())
})