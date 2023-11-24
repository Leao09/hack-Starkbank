import Link from 'next/link';
import styles from '../styles/Icon.module.css';

const Icon = () => {
    return (
        <div className={styles.iconContainer}>
            <Link href="/instructions">
                <img src="/bot.png" alt="Logo"/>    
            </Link>
        </div>
      );
    }

export default Icon;
