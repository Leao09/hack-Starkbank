import Link from 'next/link';
import styles from '../styles/Search.module.css';
import { FaSearch } from 'react-icons/fa';

const Search = () => {
    return (
        <div className={styles.searchContainer}>
            <FaSearch className={styles.searchIcon} />
            <input
              className={styles.searchInput}
              type="text"
              placeholder="Pesquisar..."
            />
          </div>
      );
    }

export default Search;
