import { ReactNode } from 'react';
import Checkable from '../_reusables/Checkable';
import { TranslationProps } from '../../i18n';
import { ResponsiveProps } from '../..';

interface RadioProps extends TranslationProps, ResponsiveProps {
  checked: boolean,
  check: (key: string, value: string) => void
  name: string,
  label: ReactNode
}

export default function Radio({t, checked, check, name, label, isMobile}: RadioProps) {
  return <div onClick={() => check('shipping', name)} className={'d-flex m-sm-3 mb-3 p-3 bg-white align-items-center w-' + (isMobile ? '100' : '50')}>
    <Checkable checked={checked} onChecked={() => check('shipping', name)} value='' />
    <span className='mx-2 h6'>{t(name)}</span>
    <span className='text-secondary flex-grow-1 d-flex justify-content-end'>
      {label}
    </span>
  </div>
}