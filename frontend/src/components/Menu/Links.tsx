import { Link } from "react-router-dom";
import { TranslationProps } from "../../i18n";
import Hoverable from "../_reusables/Hoverable";

interface Href {
  text: string,
  href: string
}

export default function Links({t}: TranslationProps) {
  const links: Href[] = [
    {text: 'home', href: '/'},
    {text: 'products', href: '/shop/folding_bed/'},
    {text: 'about', href: '/about'},
    {text: 'contacts', href: '/contacts'}
  ]

  return links.map((link, i) => 
    <Link key={i} to={link.href} className='text-decoration-none py-3 py-sm-0 me-2 ms-sm-0'>
      <Hoverable color='blue'>{t(link.text)}</Hoverable>
    </Link>
  )
}