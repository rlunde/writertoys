var NamesList = React.createClass({
    render: function() {
        return (
            <div className="namesList">
                <div className="nameFormItem">Number of names:
                    <input className="numberText" type="number" id="numNames"></input>
                </div>
                <div className="nameFormItem">Type of names:
                    <select className="nameGenders" id="nameGender">
                        <option value="female">female</option>
                        <option value="male">male</option>
                        <option value="any">any</option>
                    </select>
                </div>
                <button onClick={this.handleClick} className="namesButton">Get Names!</button>
            </div>
        );
    },
    handleClick: function() {
        var gender = $('nameGender').val();
        var number = $('numNames').val();
        alert("calling getnames with gender " + gender + " and number " + number");
        getnames(gender, number);
    }
});
ReactDOM.render(< NamesList / >, document.getElementById('names'));
