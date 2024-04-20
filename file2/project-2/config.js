const mongoose=require('mongoose')
mongoose.connect('mongodb://0.0.0.0:27017/demo')
const db=mongoose.connection
db.on('connected',()=>{
    console.log('connection to mongodb')
})

