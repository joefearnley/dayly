<?php

namespace App\Livewire;

use App\Models\Entry;
use LivewireUI\Modal\ModalComponent;

class PreviewEntry extends ModalComponent
{
    public int $entryId;
    public string $entryDate;
    public string $entryBody;

    public function mount($entryId, $entryDate, $entryBody)
    {
        $this->entryId = $entryId;
        $this->entryDate = $entryDate;
        $this->entryBody = $entryBody;
    }

    public function render()
    {
        return view('livewire.preview-entry');
    }

    public static function closeModalOnEscape(): bool
    {
        return false;
    }

    public static function closeModalOnClickAway(): bool
    {
        return false;
    }
}
