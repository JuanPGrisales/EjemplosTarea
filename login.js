class loginCompañia {
    
    constructor() {
        this.users = []         
    }

    createUser(userName, password) {
        this.users.push(new user(userName, password))
    }
    loginUser(userName, password) {
        let resultado = false
        this.users.forEach(user => {
            if(user.userName == userName){
                if(user.password == password){
                    resultado = true
                }
            }
        });      
        return resultado
    }
}

class user {
    constructor(userName, password){
        this.userName = userName
        this.password = password
    }
}

let loginNoxiun = new loginCompañia()

let userName = "PEPE"
let password = "12345"

loginNoxiun.createUser(userName, password)
console.log(loginNoxiun.loginUser(userName, password))
console.log(loginNoxiun.loginUser(userName, "456"))
