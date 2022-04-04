class ContactInfo {
	constructor(name,phone,email){
		this.Fullname= name;
		this.Phone = phone;
		this.Email = email;
	}
	
}
class Prof_desc {
	constructor(title, summary, intrest){
		this.Title= title;
		this.Sum = summary;
		this.int = intrest;
	}
}
class Education {

	constructor(Time, school,gpa, degree){
		this.TIME = Time;
		this.DEG = degree;
		this.SCH = school;
		this.GPA = gpa;
	}
	
}
class Experience{
	constructor(title,agency,time,achieve, ){
		this.Title= title;
		this.Time = time;
		this.achieve = achieve;
		this.agency=agency;
	}
}
class Extra{
	constructor(prog,  skill,language){
		this.Prog=prog;
		this.Skill=skill;
		this.Lang=language;

	}
	
}
async function loadConfigData(){
	const {default:data}=await import('./cs.json',{
		assert:{
			type:"json"
		}
	});
	var CV1 = new ContactInfo(data[0].Name,data[0].Number,
		data[0].Email);
	
	document.getElementById("Myname").innerHTML =
	CV1.Fullname+"<br>";

	document.getElementById("Contact").innerHTML =
	CV1.Phone + " " +" | " + " " +CV1.Email +"<br>";
	
	var CV2 = new Prof_desc(data[0].Prof_title,data[0].Prof_Sum,
		data[0].Res_Int);
	document.getElementById("Profesion").innerHTML =
	CV2.Title +"<br>";
	document.getElementById("Prof des").innerHTML =
	CV2.Sum +"<br>";
	
	document.getElementById("Int").innerHTML =
	CV2.int +"<br>";
	var CV3 = new Education(data[0].Edu_time,data[0].Edu_School,
		data[0].Edu_GPA,data[0].Edu_Degree);
		document.getElementById("Edu").innerHTML =
		CV3.SCH +" | "+CV3.TIME+"<br><br>"+CV3.DEG +"<br><br>"+
		CV3.GPA;
	var CV4 = new Experience(data[0].Exp_title,data[0].Exp_Agency,
		data[0].Exp_Time,data[0].Exp_Achieve);
		document.getElementById("Exp").innerHTML =
		CV4.Title+" | "+CV4.Time +"<br><br>"+
		CV4.agency +"<br><br>"+CV4.achieve;
	var CV5 = new Extra(data[0].Skills_progl,data[0].Skills,
		data[0].Lang);
		document.getElementById("Skills").innerHTML =
		CV5.Skill+" <br><br>"+CV5.Prog+" <br><br> Languages: "+CV5.Lang+" <br><br><br>";
}
loadConfigData();
