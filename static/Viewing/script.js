let a1=document.getElementById("contact-type")
let b1=document.getElementById("contact_number")
a1.addEventListener("change",y=(e)=>{
    c=a1.value
    if(c=="phone"){
        b1.type="number";
    }
    else if(C=="email"){
        b1.type="email"
    }
    else{
        b1.type="text"
    }
})

let z1=document.getElementById("mail-details")
let z2=document.getElementById("sms-details")
let r=document.getElementById("contact-type")
z1.style.display="none"
z2.style.display="none"
let b=document.getElementById("form-change")
r.addEventListener("change",i=()=>{
    p=r.value
    let y1=document.getElementById("subject")
    let y2=document.getElementById("mail-body")
    let y3=document.getElementById("sms")
    if(p==="email"){
        z2.style.display="none"
        z1.style.display="block"
        y3.removeAttribute('required')
        b.classList.add("extend2")
        b.classList.remove("extend3")
    }
    else if(p==="sms-o"){
        z1.style.display="none"
        z2.style.display="block"
        y1.removeAttribute('required')
        y2.removeAttribute('required')
        b.classList.add("extend3")
        b.classList.remove("extend2")
    }
    else{
        z1.style.display="none"
        z2.style.display="none"
        b.classList.remove("extend3")
        b.classList.remove("extend2")
    }
})

let a=document.getElementById("sub")
let con=document.getElementById("contact_number")
a.disabled=true
con.addEventListener("change",F=()=>{
    if(con.value === "")
        a.disabled=true
    else{ 
        a.disabled=false
        a.addEventListener("click",x=()=>{
            let dis=document.getElementById("after-sub")
            let spm=document.getElementById("form-change")
            dis.classList.remove("active")
            spm.classList.add("extend")
            a.classList.add("active")
            b1.readOnly=true
            a1.disabled=true
        })
    }
})