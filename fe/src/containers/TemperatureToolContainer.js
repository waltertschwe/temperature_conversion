import React, { Component } from "react";

/* Import Components */
import Input from "../components/Input";
import Select from "../components/Select";
import Button from "../components/Button";

class TemperatureToolContainer extends Component {
  constructor(props) {
    super(props);

    // set initial state
    this.state = {
      formData: {
        input_temp : "",
        convert_from : "Fahrenheit",
        convert_to : "Celsius",
        student_response : "",
      },
      results : [],
      temperatureOptions : ["Fahrenheit", "Celsius", "Kelvin", "Rankine"]
    }

    this.handleInput = this.handleInput.bind(this);
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
    this.handleClearForm = this.handleClearForm.bind(this);
  }

  handleClearForm(e) {
    e.preventDefault();
    this.setState({
      formData: {
        input_temp : "",
        convert_from : "Fahrenheit",
        convert_to : "Celsius",
        student_response : "",
      },
      results: []
    });
   }

  handleInput(e) {
    let value = e.target.value;
    let name = e.target.name;
    this.setState(
      prevState => ({
        formData: {
          ...prevState.formData,
          [name]: value
        }
      }),
      () => console.log("updated data = ", this.state.formData)
    );
  }

  // form submissions
  handleFormSubmit(e) {
    e.preventDefault();

    // get form data
    let formData = this.state.formData
    let convert_from = formData.convert_from.toLowerCase();
    let convert_to = formData.convert_to.toLowerCase();
    let input_temp = formData.input_temp;
    let student_response = formData.student_response;
    let data = {}

    // basic validation
    if (!input_temp) {
      alert("Please add an Input Temperature");
      return false;
    }

    if (!student_response) {
      alert("Please add an Student Response");
      return false;
    }

    if (convert_from === convert_to) {
      alert("Conversion Types can't match");
      return false;
    } else {
      let conversion_type = convert_from + "_to_" + convert_to

      data.converstion_type = conversion_type
      data.input_temp = parseFloat(input_temp)
      data.student_response = parseFloat(student_response)
    }

    const apiUrl = process.env.REACT_APP_API_URL + "/temperature"
    console.log("submitted form data = ", JSON.stringify(data))
    fetch(apiUrl, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      }
    })
    .then(response => response.json())
    .then(data => {
      //this.setState({results: data.lowest_cost_ndc})
      console.log("data = ", data)
    })
    .catch(error => console.error(error))
  }

  render() {
    return (
      <div className="container-fluid">
      <div className="row mt-5">
        <div className="col-md-12"></div>
      </div>
        <div className="row">
          <div className="col-md-4">
             <div className="card">
                <div className="card-header bg-success">Test Student Response</div>
                  <div className="card-body text-secondary">
                  <span className="card-text">
                  <form className="container-fluid" onSubmit={this.handleFormSubmit}>
                    <Input
                      inputtype={"text"}
                      title={"Temperature"}
                      name={"input_temp"}
                      value={this.state.formData.input_temp}
                      placeholder={"Enter Temperature"}
                      onChange={this.handleInput}
                    />{" "}
                    {/* Input Temperature */}
                    <Select
                      title={"Convert From"}
                      name={"convert_from"}
                      defaultValue={this.state.formData.convert_from}
                      //value={this.state.formData.price_code}
                      options={this.state.temperatureOptions}
                      placeholder={"Select Temperature Unit of Measure"}
                      onChange={this.handleInput}
                    />{" "}
                    {/* Unit of Measure to Convert From */}
                    <Select
                      title={"Convert To"}
                      name={"convert_to"}
                      defaultValue={this.state.formData.convert_to}
                      //value={this.state.formData.price_code}
                      options={this.state.temperatureOptions}
                      placeholder={"Select Temperature Unit of Measure"}
                      onChange={this.handleInput}
                    />{" "}
                    {/*  Unit of Measure to Convert To */}
                   {/*Submit */}
                   <Input
                     inputtype={"text"}
                     title={"Student Response"}
                     name={"student_response"}
                     value={this.state.formData.student_response}
                     placeholder={"Student Response"}
                     onChange={this.handleInput}
                   />{" "}
                   <Button
                     action={this.handleFormSubmit}
                     type={"primary"}
                     title={"Submit"}
                     style={buttonStyle}
                   />{" "}
                   <Button
                     action={this.handleClearForm}
                     type={"secondary"}
                     title={"Clear"}
                     style={buttonStyle}
                     />{" "}
                   {/* Clear the form */}
                   </form>
                   </span>
                 </div>
               </div>
           </div>
           <div className="col-md-8">
             <h3>Temperature Results </h3>

           </div>
        </div>
      </div>
     );
   }
 }

 const buttonStyle = {
 margin: "10px 10px 10px 10px"
 };

 export default TemperatureToolContainer;
