import React from 'react';
import styles from '../styles/Search.module.css';
import { FaSearch } from 'react-icons/fa';

const Search = ({ onChange }) => {
    return (
        <div className={styles.searchContainer}>
            <FaSearch className={styles.searchIcon} />
            <input
              className={styles.searchInput}
              type="text"
              placeholder="Pesquisar..."
              onChange={onChange}
            />
        </div>
    );
}

export default Search;
