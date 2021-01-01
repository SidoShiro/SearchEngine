import React from 'react';
import searchIcon from './searchIcon.png';
import './App.css';

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            search: '',
            results: ''
        };

        this.handleChange = this.handleChange.bind(this);
    }


    handleChange(e) {
        e.preventDefault();
        const {name, value} = e.target;
        this.setState({[name]: value});
    }

    render() {
        const {search} = this.state;
        return (
            <div className="App">
                <header className="App-header">
                    <h3>
                        Search Engine
                    </h3>
                    <div>
                        <form>
                            <img className={"top-menu-elt icon-search btn"} src={searchIcon} alt={"Search"}/>
                            <input type="text" className="form-control" name="search"
                                   value={search}
                                   onChange={this.handleChange}/>
                        </form>
                    </div>
                    {search !== '' ? <div><p>Search for '{search}'</p></div> : null}
                    <div>
                        <p>Results : Format</p>
                        <p>File Name : Loc</p>
                        <p>Meta</p>
                    </div>
                </header>
            </div>
        );
    }
}

export default App;
