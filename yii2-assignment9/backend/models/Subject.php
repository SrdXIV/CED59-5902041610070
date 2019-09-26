<?php
namespace backend\models;

use yii\behaviors\TimestampBehavior;
use yii\behaviors\BlameableBehavior;

class Subject extends \common\models\Subject
{
    public function behaviors()
    {
        return 
        [
            TimestampBehavior::class,//created_at and updated_at
            BlameableBehavior::class //created_by and updated_by
        ];
    }

}
