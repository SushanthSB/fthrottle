import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
    state = {
        val: "",
        ac_list: []
    }

    query(e) {
        const val = e.target.value;
        this.setState({val: val});
        const parent_this = this;

        // let url = `localhost:8000/search?word=${val}`;
        let url = `${window.location.origin}/search?word=${val}`
        fetch(url)
        .then( response => {
            return response.json();
        }).then( json => {
            if(parent_this.state.val === "")
                parent_this.setState({ac_list: []});
            else
                parent_this.setState({ac_list: json.data});
        });

    }

    getAutoCompleteElements(elements) {
        if(elements.length === 0)
            return;
        const list = elements.map((val, index) => {
            return <span key={index} className='result-element' >{val}</span>
        });
        return (
            <span className='result-container'>
                {list}
            </span>
        );
    }

    render() {
        return (
            <div className="App">
                <img src={logo} className="App-logo" alt="logo" />
                <h4>Type below for autocomplete</h4>
                <input 
                    className='search-box' 
                    type='text'
                    placeholder='start typing...'
                    onChange={(e) => this.query(e)} value={this.state.val} 
                />
                {this.getAutoCompleteElements(this.state.ac_list)}
            </div>
        );
    }
}

export default App;
