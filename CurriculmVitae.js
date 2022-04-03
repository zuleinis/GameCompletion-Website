class ContactInfo {
	constructor(Fullname, Address, Phone, Email){
		this.Fullname = Fullname;
		this.Address = Address;
		this.Phone = Phone;
		this.Email = Email;
	}
	present(data){
	}
	set(name,address,phone,email){
		this.Fullname= name;
		this.Address = address;
		this.Phone = phone;
		this.Email = email;
	}
}
class Education {
	constructor(time, school, degree){
		this.time = time;
		this.degree = degree;
		this.school = school;
	}
}
class Experience extends Education {
	constructor(time, title, achieve, agency){
		super(time);
		this.title= title;
		this.achieve = achieve;
		this.agency=agency;
	}
}
class Extra extends Experience{
	constructor(title,Res_int,Cert_prog, Cert, Skill,Lang){
		super(title);
		this.RIntrest=Res_int;
		this.Certificate=Cert;
		this.Certificate_Prog=Cert_prog;
		this.Skill=Skill;
		this.language=Lang;

	}
	
}



Papa.parse('cs.csv',
	{
	download: true,
	header: true,
	skipEmptyLines: true,
	complete: function(results){
		var Norbert = new ContactInfo(results.data[0].Name,results.data[0].Address,results.data[0].Number,results.data[0].Email);
						
	}
});
document.getElementById("demo").innerHTML =
Norbert.Fullname + " " + Norbert.Phone+ " " + Norbert.Address+ " " + Norbert.Email;