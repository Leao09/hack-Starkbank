import styles from '../styles/User.module.css';

const User = () => {
    return (
        <div className={styles.userProfile}>
            <img src="/profile.png" alt="User" className={styles.userPhoto} />
            <span className={styles.userName}>Usuário X</span>
          </div>
      );
    }

export default User;
