var NamesList = React.createClass({
    getInitialState: function() {
        return {number: '', gender: ''};
    },
    handleGenderChange: function(e) {
        this.setState({gender: e.target.value});
    },
    handleNumberChange: function(e) {
        this.setState({number: e.target.value});
    },
    render: function() {
        return (
            <div className="namesList">
                <div className="nameFormItem">Number of names:
                    <input className="numberText" type="text" placeholder="number of names" value={this.state.number} onChange={this.handleNumberChange}/>
                </div>
                <div className="nameFormItem">Type of names:
                    <select className="nameGenders" value={this.state.gender} onChange={this.handleGenderChange}>

                        <option value="female">female</option>
                        <option value="male">male</option>
                        <option value="any">any</option>
                    </select>
                </div>
                <button onClick={this.handleClick} className="namesButton">
                    Get Names !</button >
            </div>
        );
    },
    handleClick: function() {
        var gender = this.state.gender.trim();
        var number = this.state.number.trim();
        alert("calling getnames with gender " + gender + " and number " + number);
        getnames(gender, number);
    }
});
