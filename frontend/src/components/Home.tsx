import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import HoverableImage from './_reusables/HoverableImage';
import SideText from './_reusables/SideText';
import { LinksProps } from '..';
import Centralizer from './_reusables/Centralizer';

export default function Home({links}: LinksProps) {
  const [t, i18n] = useTranslation('links')

  return <Centralizer>
    <div className='d-flex flex-column align-items-center p-5 h3 text-white'>
      <SideText text='home' right='10' />
      {links.map((link, i) => {
        return <Link key={i} to={'/shop/' + link.name}>
          <HoverableImage key={i} className='mb-5' innerClassName='d-flex justify-content-center align-items-center text-whitesmoke' src={link.image}>
            <span>
              {t(link.name + '.name')}
              <sup>{link.count}</sup>
            </span>
          </HoverableImage>
        </Link>
      })}
    </div>
  </Centralizer>
}