import React, { Component } from 'react';

class WriterToysMenu extends Component {
    state = {  }
    render() {
        return (
            <ul className="wtmenu">
            <li id="genCharacters">Character</li>
            <ul className="charmenu">
            <li id="genCharNames">Names</li>
            <li id="genCharBios">Bios</li>
            </ul>
            <li id="genPlots">Plots</li>
            <li id="genLogLines">Log lines</li>
            <li id="genSettings">Settings</li>
            </ul>
        );
    }
}

export default WriterToysMenu;