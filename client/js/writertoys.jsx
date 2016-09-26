var NamesList = React.createClass({
    render: function() {
        return (
            <div className="namesList">
              <span>Number of names: </span>
                <input className="numberText" type="number" id="numNames"></input>
                <span>Type of names: </span>
                <select className="nameGenders" id="nameGender">
                    <option value="female">female</option>
                    <option value="male">male</option>
                    <option value="any">any</option>
                </select>
                <button className="namesButton">Get Names!</button>
            </div>
        );
    }
});
ReactDOM.render(< NamesList / >, document.getElementById('names'));
