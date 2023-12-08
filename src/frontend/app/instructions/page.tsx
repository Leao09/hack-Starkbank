"use client";
import Link from 'next/link'
import styles from '../styles/Instructions.module.css';
import Image from 'next/image';
import '../globals.css';


export default function History() {

    return (
      <div className={styles.container}>
        <div className={styles.instructionsContainer}>
          <p className={styles.title}>Instruções básicas para utilizar o Nav-bot:</p>
          <p className={styles.text}>Para utilizar o Nav-bot, é preciso saber de algus pontos de usabilidade e de interface, sendo eles:</p>
          <p className={styles.text}>1- Rúidos podem atrapalhar as pesquisas por audio. Assim se possivel abafar o microfone ou falar o mais próximo possivel </p>
          <p className={styles.text}>2-Algumas perguntas podem não ser reconhecidas por isso tente se baser no modelo de uso ao lado.</p>

          <Link href="/chatbot" className={styles.button}>
              <Image src="/iconNoBorder.png" alt="Play" width={40} height={40} />
              <span>Iniciar</span>
          </Link>

        </div>

        <div className={styles.botContainer}>
          <img className={styles.image} src="/botExample.png" alt="Bot"/>
        </div>

      </div>
    );
  }