import { ReactNode } from "react";
import Checkable from "../_reusables/Checkable";
import { TranslationProps } from "../../i18n";

interface RadioProps extends TranslationProps {
  checked: boolean,
  check: (key: string, value: string) => void
  name: string,
  label: ReactNode
}

export default function Radi({t, checked, check, name, label}: RadioProps) {
  return <div onClick={() => check('shipping', name)} className='d-flex m-3 p-3 w-50 bg-white align-items-center'>
    <Checkable checked={checked} onChecked={() => check('shipping', name)} value='' />
    <span className='mx-2 h6'>{t(name)}</span>
    <span className='text-secondary flex-grow-1 d-flex justify-content-end'>
      {label}
    </span>
  </div>
}