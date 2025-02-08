import React, { useState, useEffect } from 'react';
import useAutoSuggest from '../api/autosuggest';

const AutoSuggestComponent: React.FC = () => {
    const [query, setQuery] = useState('');
    const [suggestions, setSuggestions] = useState<string | null>(null);
    const { getAutoSuggest } = useAutoSuggest();

    useEffect(() => {
        const fetchSuggestions = async () => {
            if (query.length >= 3) { // Only search when len > 3
                const response = await getAutoSuggest(query);
                if (response.error) {
                    setSuggestions(`Error: ${response.error}`);
                } else {
                    setSuggestions(response.data);
                }
            } else {
                setSuggestions(null);
            }
        };

        fetchSuggestions();
    }, [query, getAutoSuggest]);


    return (
        <div>
            <div>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search"
                    style={{ width: '500px', padding: '10px', marginBottom: '10px', backgroundColor: 'white', color: 'black' }}
                />
                <div style={{padding: '10px', width: '500px', minHeight: '50px', backgroundColor: '#434343', color: '#fff' }}>
                    {suggestions ? suggestions : ''}
                </div>
            </div>
        </div>
    );
};

export default AutoSuggestComponent;