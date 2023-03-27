let a=document.getElementById("contact-owner")
a.addEventListener("change",x=(e)=>{
    let b1=document.getElementById("person-name")
    let b2=document.getElementById("company-name")
    let b3=document.getElementById("form-change")
    let r1=document.getElementById("name")
    let r2=document.getElementById("company")
    let c=a.value
    if(c=="person"){
        b3.classList.remove("extend")
        b2.classList.add("active")
        b1.classList.remove("active")
        r2.removeAttribute('required')
    }
    else if(c=="company"){
        b3.classList.remove("extend")
        b1.classList.add("active")
        b2.classList.remove("active")
        r1.removeAttribute('required')
    }
    else{
        b1.classList.add("active")
        b2.classList.add("active")
        b3.classList.add("extend")
    }
})   

let a1=document.getElementById("contact-type")
a1.addEventListener("change",y=(e)=>{
    let b1=document.getElementById("contact_number")
    c=a1.value
    if(c=="phone"){
        b1.type="number";
    }
    else{
        b1.type="email"
    }
})

let slider=document.getElementById("myRange")
let output=document.getElementById("demo")
output.innerHTML=slider.value;
slider.addEventListener("input",func=(e)=>{
    output.innerHTML=slider.value;
})

let spm=document.getElementById("spam-NO")
spm.addEventListener("click",sp=()=>{
    let y=document.getElementById("slide")
    y.style.display="none"
    let b3=document.getElementById("form-change")
    b3.classList.add("reduce")
})

let sm=document.getElementById("spam-yes")
sm.addEventListener("click",p=()=>{
    let y=document.getElementById("slide")
    y.style.display="block"
    let b3=document.getElementById("form-change")
    b3.classList.remove("reduce")
})

let z1=document.getElementById("mail-details")
let z2=document.getElementById("sms-details")
let r=document.getElementById("contact-type")
z1.style.display="none"
z2.style.display="none"
r.addEventListener("change",i=()=>{
    p=r.value
    let y1=document.getElementById("subject")
    let y2=document.getElementById("mail-body")
    let y3=document.getElementById("sms")
    let b=document.getElementById("form-change")
    if(p==="email"){
        z2.style.display="none"
        z1.style.display="block"
        y3.removeAttribute('required')
        b.classList.add("extend2")
        b.classList.remove("extend3")
    }
    else if(p==="phone"){
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